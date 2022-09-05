import arcade
import fetch_data

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Pokemon"


class PokemonSprite(arcade.Sprite):

    def __init__(self, pokemon):

        # Pass arguments to class arcade.Sprite
        super().__init__()

        self.idle = pokemon.get_asset("idle.png")

        self.texture = arcade.load_texture(self.idle)


    def update(self, delta_time):
        self.center_x = 300
        self.center_y = 250


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.pokemon_sprite = None
        self.pokemon = None

    def setup(self):
        arcade.start_render()
        self.pokemon = fetch_data.get_pokemon("pikachu")

        self.pokemon_sprite = PokemonSprite(
            pokemon=self.pokemon
        )

    def on_draw(self):

        self.clear()
        self.pokemon_sprite.draw()


    def on_update(self, delta_time):
        self.pokemon_sprite.update(delta_time)


    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
