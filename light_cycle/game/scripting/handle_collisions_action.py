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
        score1 = cast.get_first_actor("scores")
        score2 = cast.get_last_actor("scores")
        cycle1 = cast.get_first_actor("cycles")
        cycle2 = cast.get_last_actor("cycles")
        trail1 = cycle1.get_segments()
        trail2 = cycle2.get_segments()
        head1 = cycle1.get_head()
        head2 = cycle2.get_head()

        for segment in trail2:
            if head1.get_position().equals(segment.get_position()):
                score2.add_points(1)
                self._is_game_reset = True

        for segment in trail1:
            if head2.get_position().equals(segment.get_position()):
                score1.add_points(1)
                self._is_game_reset = True

    # Owner: Evan Thomson
    def _handle_cycle_cycle_collision(self, cast):
        """Sets the game reset flag if the cycle collides with another cycle.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycles")
        cycle2 = cast.get_last_actor("cycles")

        head1 = cycle1.get_head()
        head2 = cycle2.get_head()

        if head1.get_position().equals(head2.get_position()):
            self._is_game_reset = True

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

            self._is_game_reset = False