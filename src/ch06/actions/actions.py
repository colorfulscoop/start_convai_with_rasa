from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):
    def __init__(self):
        self._recommend_db = {
            ("フランス", "赤"): "ジュヴレ・シャンベルタン",
            ("フランス", "白"): "ムルソー",
            ("アメリカ", "赤"): "ナパ・ヴァレー",
            ("アメリカ", "白"): "ソノマ",
        }

    def name(self) -> Text:
        return "action_show_recommended_wine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # スロットの値を取得します
        country = tracker.get_slot("country_slot")
        wine_type = tracker.get_slot("wine_type_slot")

        # スロットの値から検索を実行します
        key = (country, wine_type)
        recommend = self._recommend_db[key]

        # dispatcher.utter_messageを使って応答発話を行います
        dispatcher.utter_message(text=f"{country}の{recommend}の{wine_type}ワインはいかがでしょうか？")

        # SlotSetイベントを戻り値に設定してスロットを初期化します
        return [SlotSet("country_slot", None), SlotSet("wine_type_slot", None)]
