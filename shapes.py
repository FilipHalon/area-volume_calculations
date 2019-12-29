from math import pi, sqrt


class Rectangle:
    def __init__(self, side_a, side_b=None):
        self.side_a = side_a
        self.side_b = side_a if not side_b else side_b

    def calculate_area(self):
        return self.side_a * self.side_b


class RectangleAreaMixin(Rectangle):
    def calculate_rectangle_area(self):
        return super().calculate_area()


class Triangle(Rectangle):
    def __init__(self, side, height):
        super().__init__(side, height)

    def calculate_area(self):
        return super().calculate_area()/2


class Cube(Rectangle):
    def __init__(self, side):
        super().__init__(side)

    def calculate_area(self):
        return super().calculate_area() * 6

    def calculate_volume(self):
        return super().calculate_area() * self.side_a


class RegularPyramid(Triangle, RectangleAreaMixin):
    def __init__(self, pyramid_height, base_num_of_sides, base_side):
        super().__init__(base_side, base_side)
        self.base_num_of_sides = base_num_of_sides
        if self.base_num_of_sides == 3:
            self.side_b = self.side_b * sqrt(3) / 2
        self.pyramid_height = pyramid_height
        self.__base_area = self.calculate_base_area()

    def calculate_edge_length(self):
        return sqrt(self.side_a ** 2 / 3 + self.pyramid_height ** 2)

    def calculate_slant_height(self):
        if self.base_num_of_sides == 3:
            return sqrt((4 * self.calculate_edge_length() ** 2 - self.side_a ** 2)/4)
        else:
            return sqrt((self.side_b / 2) ** 2 + self.pyramid_height ** 2)

    def calculate_base_area(self):
        if self.base_num_of_sides < 3:
            raise ValueError("This is not a three-dimensional shape.")
        elif self.base_num_of_sides == 3:
            return super().calculate_area()
        elif self.base_num_of_sides == 4:
            return super().calculate_rectangle_area()
        else:
            raise ValueError("Unsupported number of sides. No more than 4 is supported.")

    @property
    def base_area(self):
        return self.__base_area

    def calculate_area(self):
        slant = Triangle(self.side_a, self.calculate_slant_height())
        return self.__base_area + slant.calculate_area() * self.base_num_of_sides

    def calculate_volume(self):
        return self.__base_area * self.pyramid_height / 3


class Ellipse(Rectangle):
    def __init__(self, major_r, minor_r):
        super().__init__(major_r, minor_r)

    def calculate_area(self):
        return super().calculate_area() * pi
