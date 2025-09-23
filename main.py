from controllers.models.user_model import UserModel
from controllers.user_controller import UserController

if __name__ == "__main__":
    user_model = UserModel()
    user_controller = UserController(user_model)
    user_controller.start()