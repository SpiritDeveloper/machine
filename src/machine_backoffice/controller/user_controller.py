from fastapi import APIRouter
from ..services.user_service import UserService
from ..utils.documentation import Documentation
from ..config.dto.types import RequestMethodEnum
from ..dto import CreateUserInputSchema, CreateUserInput, UpdateUserInput, UpdateUserInputSchema

user = APIRouter(prefix="/user", tags=["user"])


class UserController:
    get_user_by_id_documentation = Documentation.create(
        message="Get information of user by id",
        method=RequestMethodEnum.GET,
        payload={},
        authorization=True,
    )

    @user.get(
        "/get/{id}",
        description="Returns a user by id",
        responses=get_user_by_id_documentation,
    )
    def get_user(id: str):
        return UserService().get(id)

    get_all_users_documentation = Documentation.create(
        message="Get all users",
        method=RequestMethodEnum.GET,
        payload={},
        authorization=True,
    )

    @user.get(
        "/get",
        description="Returns all users",
        responses=get_all_users_documentation,
    )
    def get_all_users():
        return UserService().get_all()

    create_user_documentation = Documentation.create(
        message="Create a new user",
        method=RequestMethodEnum.POST,
        payload=CreateUserInputSchema,
        authorization=True,
    )

    @user.post(
        "/create",
        description="Creates a new user",
        responses=create_user_documentation,
    )
    def create_new_user(create: CreateUserInputSchema):
        create: CreateUserInputSchema = CreateUserInput.create(create)
        return UserService().create(create)

    update_user_documentation = Documentation.create(
        message="Update a user",
        method=RequestMethodEnum.PUT,
        payload=UpdateUserInputSchema,
        authorization=True,
    )

    @user.put(
        "/update/{id}",
        description="Updates a user",
        responses=update_user_documentation,
    )
    def update_user(id: str, update: UpdateUserInputSchema):
        update: UpdateUserInputSchema = UpdateUserInput.create(update)
        return UserService().update(id, update)

    delete_user_documentation = Documentation.create(
        message="Delete a user",
        method=RequestMethodEnum.DELETE,
        payload={},
        authorization=True,
    )

    @user.delete(
        "/delete/{id}",
        description="Deletes a user",
        responses=delete_user_documentation,
    )
    def delete_user(id: str):
        return UserService().delete(id)