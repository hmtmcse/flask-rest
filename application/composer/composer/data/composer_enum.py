from pfms.common.enum_processor import BaseEnum


class PageUseFor(BaseEnum):
    Mobile = "Mobile"
    Web = "Web"


class PageLayout(BaseEnum):
    Default = "Default"


class PageType(BaseEnum):
    Index = "Index"
    Other = "Other"


class PageWidgetLayoutType(BaseEnum):
    NONE = "NONE"
    List = "List"
    Grid = "Grid"


class PageWidgetScroll(BaseEnum):
    NONE = "NONE"
    Horizontal = "Horizontal"
    Vertical = "Vertical"


class PageWidgetSizeUnit(BaseEnum):
    NONE = "NONE"
    Percentage = "Percentage"
    Pixel = "Pixel"


class PageWidgetShape(BaseEnum):
    NONE = "NONE"
    RoundCorner = "RoundCorner"
    Circle = "Circle"
    Rectangle = "Rectangle"


class WidgetType(BaseEnum):
    Item = "Item"
    ItemGroup = "ItemGroup"
    Supplier = "Supplier"
    SupplierGroup = "SupplierGroup"
    Card = "Card"


class CardType(BaseEnum):
    Slider = "Slider"
    Thumb = "Thumb"
    TextOnly = "TextOnly"


class NavigationUseFor(BaseEnum):
    Web = "Web"
    Mobile = "Mobile"


class NavigationNavType(BaseEnum):
    Main = "Main"
    Header = "Header"
    Other = "Other"
