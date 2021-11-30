import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from light_cycle.constants import WHITE

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the trail, or when the cycle collides with another cycle, or when the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_cycle_trail_collision(cast)
            self._handle_cycle_cycle_collision(cast)
            self._handle_game_over(cast)

    def _handle_cycle_trail_collision(self, cast):
        """Updates the score and moves the trail if the cycle collides with the trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # score = cast.get_first_actor("scores")
        # trail = cast.get_first_actor("trails")
        # cycle = cast.get_first_actor("cycles")
        # head = cycle.get_head()

        # if head.get_position().equals(trail.get_position()):
        #     points = trail.get_points()
        #     cycle.grow_tail(points)
        #     score.add_points(points)
        #     trail.reset()
        pass
    
    def _handle_cycle_cycle_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its trails.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # cycle = cast.get_first_actor("cycles")
        # head = cycle.get_trails()[0]
        # trail = cycle.get_trails()[1:]
        
        # for trail in trails:
        #     if head.get_position().equals(trail.get_position()):
        #         self._is_game_over = True
        pass
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle and trail white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle = cast.get_first_actor("cycles")
            trails = cycle.get_trails()
            trail = cast.get_first_actor("trails")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for trail in trails:
                trail.set_color(WHITE)
            trail.set_color(WHITE)