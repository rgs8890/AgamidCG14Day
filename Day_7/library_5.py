# UNIQUE IDs
# uuid
# generate universally unique identifiers
# databases, file-naming, managing user sessions
import uuid

unique_id = int(uuid.uuid4())

# item = {
#     "name": name,
#     "store": store,
#     "cost": cost,
#     "amount": amount,
#     "priority": priority,
#     "buy": buy,
#     "id": unique_id
# }

# grocery_list.append(item)

# def get_item_from_id(id: int) -> int:
#     index = 0
#     for item in grocery_list:
#         if item["id"] == id:
#             return index
#         else:
#             index +=1

# def remove_item_from_id(id: int) -> int:
#     index = get_index_from_id(id)
#     grocery_list.pop(index)


# def edit_item(
#         name: str,
#         store: float | None = None,
#         cost: float | None = None,
#         amount: int | None = None,
#         priority: int | None = None,
#         buy: str | bool = "skip",
#         id: int | None = None
# ) -> None:
#     """
#     Edit an existing item in the grocery list.

#     Args:
#         name (str): _description_
#         store (float | None, optional): _description_. Defaults to None.
#         cost (float | None, optional): _description_. Defaults to None.
#         amount (int | None, optional): _description_. Defaults to None.
#         priority (int | None, optional): _description_. Defaults to None.
#         buy (str | bool, optional): _description_. Defaults to "skip".
#         id (int | None, optional): _description_. Defaults to None.
#     """

#     index = get_item_from_id(id)
#     old_item = grocery_list[index]

#     store = store if store is not None else old_item["store"]
#     cost = cost if cost is not None else old_item["cost"]
#     amount = amount if amount is not None else old_item["amount"]


import uuid
for i in range(5):
    unique_id = int(uuid.uuid4())
    print(unique_id)

# ID -> Index
# old_item["values"]