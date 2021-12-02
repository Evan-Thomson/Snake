from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.constants import MAX_X, MAX_Y

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the trail, or when the cycle collides with another cycle, or when the game resets.

    Attributes:
        _is_game_reset (boolean): Whether or not the game is reset.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_reset = False

    # Owner: Evan Thomson
    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_reset:
            self._handle_cycle_trail_collision(cast)
            self._handle_cycle_cycle_collision(cast)
            self._handle_game_reset(cast)

    # Owner: Evan Thomson
    def _handle_cycle_trail_collision(self, cast):
        """Updates the score and moves the trail if the cycle collides with the trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        trail = cast.get_first_actor("trails")
        cycle = cast.get_first_actor("cycles")
        head = cycle.get_head()

        if head.get_position().equals(trail.get_position()):
            points = trail.get_points()
            score.add_points(points)
            trail.reset()

    # Owner: Evan Thomson
    def _handle_cycle_cycle_collision(self, cast):
        """Sets the game reset flag if the cycle collides with another cycle.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle = cast.get_first_actor("cycles")
        head = cycle.get_head()[0]
        trail = cycle.get_segments()[1:]

        if head.get_position().equals(head.get_position()):
            trail.reset()

    # Owner: Evan Thomson
    def _handle_game_reset(self, cast):
        """Handles game reset when one cycle collides with another actor.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_reset:
            x = int(MAX_X / 2)
            y = int(MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game reset!")
            message.set_position(position)
            cast.add_actor("messages", message)