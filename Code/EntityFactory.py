from Code.Background import Background
from Code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg1':
                list_bg = []
                list_bg.append(Background('Level1Bg1', (0, 0)))
                list_bg.append(Background('Level1Bg1', (WIN_WIDTH, 0)))
                return list_bg


