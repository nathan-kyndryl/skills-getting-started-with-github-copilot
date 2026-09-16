from fastapi.testclient import TestClient

from src.app import activities, app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "test.student@mergington.edu"
    original_participants = list(activities[activity_name]["participants"])
    activities[activity_name]["participants"].append(email)

    try:
        # Act
        response = client.delete(
            f"/activities/{activity_name}/participants/{email}",
        )

        # Assert
        assert response.status_code == 200
        assert email not in activities[activity_name]["participants"]
        assert response.json() == {"message": f"Removed {email} from {activity_name}"}
    finally:
        activities[activity_name]["participants"] = original_participants
