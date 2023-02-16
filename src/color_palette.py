import colorgram

class Extractor:
    COLORS = []
    
    def __init__(self) -> None:
        pass

    def extract(self, img_path: str, num_of_colors: int) -> None:
        colors = colorgram.extract(img_path, num_of_colors)
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            Extractor.COLORS.append((r,g,b))
        for _ in range(3):
            Extractor.COLORS.pop(0)