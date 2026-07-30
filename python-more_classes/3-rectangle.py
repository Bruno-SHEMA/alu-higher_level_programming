    def __str__(self):
        """Return the printable representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)
