import allure
from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import (GetExercisesQuerySchema,
                                                GetExercisesResponseSchema,
                                                CreateExerciseRequestSchema,
                                                ExerciseResponseSchema,
                                                UpdateExerciseRequestSchema)
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(
            url=APIRoutes.EXERCISES,
            params=query.model_dump(by_alias=True)
        )

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании.

        :param exercise_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            url=APIRoutes.EXERCISES,
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(
            self,
            exercise_id: str,
            request: UpdateExerciseRequestSchema
    ) -> Response:
        """
        Метод обновления задания.

        :param exercise_id : Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description,
        estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            url=f"{APIRoutes.EXERCISES}/{exercise_id}",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> ExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return ExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> ExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return ExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(
            self,
            exercise_id: str,
            request: UpdateExerciseRequestSchema
    ) -> ExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return ExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
