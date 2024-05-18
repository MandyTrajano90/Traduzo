from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
from datetime import datetime
from bson import ObjectId


def test_history_delete(app_test):
    # Cria um usuário admin
    admin_user = UserModel({"name": "admin", "token": "valid_token"})
    admin_user.save()

    # Cria um histórico
    history = HistoryModel({
        "text_to_translate": "House",
        "translated": "Casa",
        "translate_from": "en",
        "translate_to": "pt",
        "timestamp": datetime.now(),
    })
    history.save()

    # Pega o ID do histórico
    history_id = str(history.data["_id"])

    # Deleta o histórico
    response = app_test.delete(f"/admin/history/{history_id}", headers={
      "Authorization": "valid_token",
      "User": "admin",
    })

    # Verifica se o status code é 204
    assert response.status_code == 204

    # Verifica se o histórico foi deletado
    assert HistoryModel.find_one({"_id": ObjectId(history_id)}) is None
