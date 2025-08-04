import dataclasses

@dataclasses.dataclass
class webex_message_user:
    id: str
    roomId: str
    toPersonEmail: str
    roomtype: str
    text: str
    personId: str
    personEmail: str
    created: str

    @staticmethod
    def from_dict(data: dict) -> "webex_message_user":
        return webex_message_user(
            id=data.get("id", ""),
            roomId=data.get("roomId", ""),
            toPersonEmail=data.get("toPersonEmail", ""),
            roomtype=data.get("roomtype", ""),
            text=data.get("text", ""),
            personId=data.get("personId", ""),
            personEmail=data.get("personEmail", ""),
            created=data.get("created", ""),
        )

    def as_dict(self) -> dict:
        return dataclasses.asdict(self)
    
@dataclasses.dataclass
class webex_list_rooms:
    items: list["webex_list_rooms_items"]

    @staticmethod
    def from_dict(data: dict) -> "webex_list_rooms":
        return webex_list_rooms(
            items=[
                webex_list_rooms_items.from_dict(item) for item in data.get("items", [])
            ]
        )

@dataclasses.dataclass
class webex_list_rooms_items:
    id: str
    title: str
    type: str
    isLocked: bool
    lastActivtiy: str
    creatorId: str
    created: str
    ownerId: str
    isPublic: bool
    isReadOnly: bool

    @staticmethod
    def from_dict(data: dict) -> "webex_list_rooms_items":
        return webex_list_rooms_items(
            id=data.get("id", ""),
            title=data.get("title", ""),
            type=data.get("type", ""),
            isLocked=data.get("isLocked", ""),
            lastActivtiy=data.get("lastActivtiy", ""),
            creatorId=data.get("creatorId", ""),
            created=data.get("created", ""),
            ownerId=data.get("ownerId", ""),
            isPublic=data.get("isPublic", ""),
            isReadOnly=data.get("isReadOnly", ""),
        )
    
    def as_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class webex_list_people:
    notFoundIds: None
    items: list["webex_list_people_items"]

    @staticmethod
    def from_dict(data:dict) -> "webex_list_people":
        return webex_list_people(
            notFoundIds=data.get("notFoundIds", None),
            items=[webex_list_people_items.from_dict(item) for item in data.get("items", [])]
        )
    
    def as_dict(self) -> dict:
        return dataclasses.asdict(self)
    

@dataclasses.dataclass
class webex_list_people_items:
    id: str
    emails: list[str]
    phoneNumbers: list[dict]
    displayName: str
    nickName: str
    firstName: str
    lastName: str
    avatar: str
    orgId: str
    created: str
    lastModified: str
    lastActivity: str
    status: str
    type: str
    department: str
    title: str
    manager: str
    managerId: str
    addresses: list[dict]

    @staticmethod
    def from_dict(data: dict) -> "webex_list_people_items":
        return webex_list_people_items(
            id=data.get("id", ""),
            emails=data.get("emails", ""),
            phoneNumbers=data.get("phoneNumbers", ""),
            displayName=data.get("displayName", ""),
            nickName=data.get("nickName", ""),
            firstName=data.get("firstName", ""),
            lastName=data.get("lastName", ""),
            avatar=data.get("avatar", ""),
            orgId=data.get("orgId", ""),
            created=data.get("created", ""),
            lastModified=data.get("lastModified", ""),
            lastActivity=data.get("lastActivity", ""),
            status=data.get("status", ""),
            type=data.get("type", ""),
            department=data.get("department", ""),
            title=data.get("title", ""),
            manager=data.get("manager", ""),
            managerId=data.get("managerId", ""),
            addresses=data.get("addresses", ""),
        )
    
    def as_dict(self) -> dict:
        return dataclasses.asdict(self)