import pytest
from src.core.game_object import GameObjectCls, Type, GameObject, Parent


class Testing:

    def test_correctly_init_game_object(self):
        player = GameObject(name="Player", object_type=Type.PLAYER)
        enemy_bob = GameObject(name="Bob", object_type=Type.NPC)
        enemy_eve = GameObject(name="Eve", object_type=Type.NPC)

        group = Parent(name="My Enemies", children=[enemy_bob, enemy_eve])
        assert player.name == 'Player'
        assert len(group.children) == 2

    def test_incorrectly_init_parent(self):
        player = GameObject(name="Player", object_type=Type.PLAYER)
        enemy_bob = GameObject(name="Bob", object_type=Type.NPC)
        enemy_eve = GameObject(name="Eve", object_type=Type.NPC)

        with pytest.raises(ValueError):
            Parent(name="My Enemies", children=[enemy_bob, enemy_eve, "abc"])

    def test_invalid_name_raises_value_error(self):
        with pytest.raises(ValueError, match="GameObject name can only contain A-Z, 0-9, _, or -"):
            GameObject(name="Player?", object_type=Type.PLAYER)  # Using GameObject, not GameObjectCls



