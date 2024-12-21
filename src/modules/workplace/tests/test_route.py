import unittest.mock
import fastapi
import sqlalchemy.exc

from workplace import main
from workplace import services as service


workplace_prefix = "/workplaces"


@unittest.mock.patch("workplace.routes.workplace.WorkplaceService")
def test_list_workplaces_route_return_empty_list(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    expected_resp = []
    main.app.dependency_overrides[service.WorkplaceService] = (
        lambda: mock_workplace_service
    )
    mock_workplace_service.get_workplaces.return_value = expected_resp

    # Act
    actual_resp: fastapi.Response = test_client.get(f"{workplace_prefix}/")
    result_workplaces = actual_resp.json()

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_200_OK
    assert len(result_workplaces) == 0
    assert result_workplaces == expected_resp


@unittest.mock.patch("workplace.routes.workplace.WorkplaceService")
def test_list_workspaces_route_return_workplace_list(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    test_workplace = {"id": 1, "name": "Ledon City", "address": "182 Hong Bang"}
    expected_resp = [test_workplace]
    main.app.dependency_overrides[service.WorkplaceService] = (
        lambda: mock_workplace_service
    )
    mock_workplace_service.get_workplaces.return_value = expected_resp

    # Act
    actual_resp: fastapi.Response = test_client.get(f"{workplace_prefix}/")
    result_workplaces = actual_resp.json()

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_200_OK
    assert len(result_workplaces) > 0
    assert result_workplaces == expected_resp


@unittest.mock.patch("workplace.routes.workplace.WorkplaceService")
def test_get_workplace_route_return_workplace_info(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    test_workplace_id = 1
    expected_resp = {"id": 1, "name": "Leon City", "address": "275 Hong Bang"}
    main.app.dependency_overrides[service.WorkplaceService] = (
        lambda: mock_workplace_service
    )
    mock_workplace_service.get_workplace_by_id.return_value = expected_resp

    # Act
    actual_resp = test_client.get(f"{workplace_prefix}/{test_workplace_id}")
    result_workplace = actual_resp.json()

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_200_OK
    assert result_workplace == expected_resp


@unittest.mock.patch("workplace.routes.workplace.WorkplaceService")
def test_get_workplace_route_cannot_find_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    test_workplace_id = 12
    expected_resp = None
    main.app.dependency_overrides[service.WorkplaceService] = (
        lambda: mock_workplace_service
    )
    mock_workplace_service.get_workplace_by_id.return_value = expected_resp

    # Act
    actual_resp = test_client.get(f"{workplace_prefix}/{test_workplace_id}")

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_404_NOT_FOUND


@unittest.mock.patch("workplace.routes.workplace.WorkplaceService")
def test_create_workplace_route_can_create_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    test_workplace = {"name": "Leon City", "address": "275 Hong Bang"}
    expected_resp = dict({"id": 1}, **test_workplace)
    main.app.dependency_overrides[service.WorkplaceService] = (
        lambda: mock_workplace_service
    )
    mock_workplace_service.create_workplace.return_value = expected_resp

    # Act
    actual_resp = test_client.post(f"{workplace_prefix}/", json=test_workplace)
    result_workplace = actual_resp.json()

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_201_CREATED
    mock_workplace_service.create_workplace.assert_called_once()
    assert result_workplace == expected_resp


@unittest.mock.patch("workplace.routes.workplace.WorkplaceService")
def test_patch_workplace_route_can_update_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    test_workplace_id = 1
    test_workplace = {"name": "Leon City", "address": "275 Hong Bang"}
    main.app.dependency_overrides[service.WorkplaceService] = (
        lambda: mock_workplace_service
    )
    mock_workplace_service.update_workplace.return_value = None

    # Act
    actual_resp = test_client.patch(
        f"{workplace_prefix}/{test_workplace_id}", json=test_workplace
    )

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_204_NO_CONTENT
    mock_workplace_service.update_workplace.assert_called_once()


@unittest.mock.patch("workplace.routes.workplace.WorkplaceService")
def test_patch_workplace_route_cannot_find_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    test_workplace_id = 1
    test_workplace = {"name": "Leon City", "address": "275 Hong Bang"}
    main.app.dependency_overrides[service.WorkplaceService] = (
        lambda: mock_workplace_service
    )
    mock_workplace_service.update_workplace.side_effect = sqlalchemy.exc.NoResultFound

    # Act
    actual_resp = test_client.patch(
        f"{workplace_prefix}/{test_workplace_id}", json=test_workplace
    )

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_404_NOT_FOUND

    mock_workplace_service.update_workplace.assert_called_once()


@unittest.mock.patch("workplace.routes.workplace.WorkplaceService")
def test_delete_workplace_route_can_delete_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    test_workplace_id = 1
    main.app.dependency_overrides[service.WorkplaceService] = (
        lambda: mock_workplace_service
    )
    mock_workplace_service.delete_workplace.return_value = None

    # Act
    actual_resp = test_client.delete(f"{workplace_prefix}/{test_workplace_id}")

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_204_NO_CONTENT

    mock_workplace_service.delete_workplace.assert_called_once()
    # No keyword argument is used in WorkplaceService.delete_workplace(),
    # so assert_called_once_with(workplace_id=test_workplace_id) is NOT valid
    mock_workplace_service.delete_workplace.assert_called_once_with(test_workplace_id)


@unittest.mock.patch("workplace.routes.workplace.WorkplaceService")
def test_delete_workplace_route_cannot_find_workplace(
    mock_workplace_service, test_client
) -> None:
    # Arrange
    test_workplace_id = 1
    main.app.dependency_overrides[service.WorkplaceService] = (
        lambda: mock_workplace_service
    )
    mock_workplace_service.delete_workplace.side_effect = sqlalchemy.exc.NoResultFound

    # Act
    actual_resp = test_client.delete(f"{workplace_prefix}/{test_workplace_id}")

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_404_NOT_FOUND

    mock_workplace_service.delete_workplace.assert_called_once()
    mock_workplace_service.delete_workplace.assert_called_once_with(test_workplace_id)


@unittest.mock.patch("workplace.routes.workplace.WorkplaceService")
def test_delete_workplace_route_cannot_delete_workplace(
    mock_workplace_service, test_client
):
    # Arrange
    test_workplace_id = 1
    main.app.dependency_overrides[service.WorkplaceService] = (
        lambda: mock_workplace_service
    )
    mock_workplace_service.delete_workplace.side_effect = Exception

    # Act
    actual_resp = test_client.delete(f"{workplace_prefix}/{test_workplace_id}")

    # Assert
    assert actual_resp.status_code == fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR

    mock_workplace_service.delete_workplace.assert_called_once()
    mock_workplace_service.delete_workplace.assert_called_once_with(test_workplace_id)
