import dataclasses

@dataclasses.dataclass
class Authorization:
    access_token: str
    refresh_token: str
    athelete_id: int
    athelete_name: str
    athelete_premium: bool

    @staticmethod
    def from_dict(data: dict) -> "Authorization":
        return Authorization(
            access_token=data.get("access_token", ""),
            refresh_token=data.get("refresh_token", ""),
            athelete_id=data.get("athelete.id", ""),
            athelete_name=data.get("athelete.name", ""),
            athelete_premium=data.get("athelete.premium", False),
        )
    
    def as_dict(self) -> dict:
        return dataclasses.asdict(self)
    
@dataclasses.dataclass
class Refresh:
    token_type: str
    access_token: str
    expires_at: int
    expires_in: int
    refresh_token: str

    @staticmethod
    def from_dict(data: dict) -> "Refresh":
        return Refresh(
            token_type=data.get("token_type", ""),
            access_token=data.get("access_token", ""),
            expires_at=data.get("expires_at", ""),
            expires_in=data.get("expires_in", ""),
            refresh_token=data.get("refresh_token", ""),
        )
    
    def as_dict(self) -> dict:
        return dataclasses.asdict(self)
    
@dataclasses.dataclass
class GetAthlete:
    id: int | None
    username: str | None
    resource_state: int | None
    firstname: str | None
    lastname: str | None
    bio: str | None
    city: str | None
    state: str | None
    country: str | None
    sex: str | None
    premium: bool | None
    summit: bool | None
    created_at: str | None
    updated_at: str | None
    badge_type_id: int | None
    weight: int | None
    profile_medium: str | None
    profile: str | None
    friend: str | None
    follower: str | None

    @staticmethod
    def from_dict(data:dict) -> "GetAthlete":
        return GetAthlete(
            id=data.get("id", ""),
            username=data.get("username", ""),
            resource_state=data.get("resource_state", ""),
            firstname=data.get("firstname", ""),
            lastname=data.get("lastname", ""),
            bio=data.get("bio", ""),
            city=data.get("city", ""),
            state=data.get("state", ""),
            country=data.get("country", ""),
            sex=data.get("sex", ""),
            premium=data.get("premium", ""),
            summit=data.get("summit", ""),
            created_at=data.get("created_at", ""),
            updated_at=data.get("updated_at", ""),
            badge_type_id=data.get("badge_type_id", ""),
            weight=data.get("weight", ""),
            profile_medium=data.get("profile_medium", ""),
            profile=data.get("profile", ""),
            friend=data.get("friend", ""),
            follower=data.get("follower", ""),
        )

    def as_dict(self) -> dict:
        return dataclasses.asdict(self)
    
@dataclasses.dataclass
class AthleteActivities:
    activities: list["AthleteActivity"]

    @staticmethod
    def from_dict(data: list[dict]) -> "AthleteActivities":
        activities = [AthleteActivity.from_dict(activity) for activity in data]
        return AthleteActivities(activities=activities)
    
    @staticmethod
    def get_activities_by_type(athlete_activities: "AthleteActivities", activity_type: str) -> "AthleteActivities":
        return AthleteActivities(activities=[activity for activity in athlete_activities.activities if activity.type == activity_type])
    
@dataclasses.dataclass
class AthleteActivity:
    resource_state: int | None
    athlete: dict | None
    name: str | None
    distance: int
    moving_time: int
    elapsed_time: int
    total_elevation_gain: int
    type: str
    sport_type: str
    workout_type: int
    id: int
    start_time: str
    start_date_local: str
    timezone: str
    utc_offset: int
    location_city: str | None
    location_state: str
    location_country: str
    achievement_count: int
    kudos_count: int
    comment_count: int
    athlete_count: int
    photo_count: int
    map: dict 
    trainer: bool 
    commute: bool
    manual: bool
    private: bool
    visibility: str
    flagged: bool
    gear_id: int | None
    start_latlng: list 
    end_latlng: list
    average_cadence: int
    average_temp: int
    average_watts: int
    max_watts: int
    weighted_average_watts: int
    device_watts: bool
    kilojoules: int
    has_heartrate: bool
    heartrate_opt_out: bool
    display_hide_heartrate_option: bool
    elev_high: int
    elev_low: int
    upload_id: int
    upload_id_str: str
    external_id: str
    from_accepted_tag: bool
    pr_count: int
    total_photo_count: int
    has_kudoed: bool

    @staticmethod
    def from_dict(data: dict) -> "AthleteActivity":
        return AthleteActivity(
            resource_state=data.get("resource_state", ""),
            athlete=data.get("athlete", ""),
            name=data.get("name", ""),
            distance=data.get("distance", ""),
            moving_time=data.get("moving_time", ""),
            elapsed_time=data.get("elapsed_time", ""),
            total_elevation_gain=data.get("total_elevation_gain", ""),
            type=data.get("type", ""),
            sport_type=data.get("sport_type", ""),
            workout_type=data.get("workout_type", ""),
            id=data.get("id", ""),
            start_time=data.get("start_time", ""),
            start_date_local=data.get("start_date_local", ""),
            timezone=data.get("timezone", ""),
            utc_offset=data.get("utc_offset", ""),
            location_city=data.get("location_city", ""),
            location_state=data.get("location_state", ""),
            location_country=data.get("location_country", ""),
            achievement_count=data.get("achievement_count", ""),
            kudos_count=data.get("kudos_count", ""),
            comment_count=data.get("comment_count", ""),
            athlete_count=data.get("athlete_count", ""),
            photo_count=data.get("photo_count", ""),
            map=data.get("map", ""),
            trainer=data.get("trainer", ""),
            commute=data.get("commute", ""),
            manual=data.get("manual", ""),
            private=data.get("private", ""),
            visibility=data.get("visibility", ""),
            flagged=data.get("flagged", ""),
            gear_id=data.get("gear_id", ""),
            start_latlng=data.get("start_latlng", ""),
            end_latlng=data.get("end_latlng", ""),
            average_cadence=data.get("average_cadence", ""),
            average_temp=data.get("average_temp", ""),
            average_watts=data.get("average_watts", ""),
            max_watts=data.get("max_watts", ""),
            weighted_average_watts=data.get("weighted_average_watts", ""),
            device_watts=data.get("device_watts", ""),
            kilojoules=data.get("kilojoules", ""),
            has_heartrate=data.get("has_heartrate", ""),
            heartrate_opt_out=data.get("heartrate_opt_out", ""),
            display_hide_heartrate_option=data.get("display_hide_heartrate_option", ""),
            elev_high=data.get("elev_high", ""),
            elev_low=data.get("elev_low", ""),
            upload_id=data.get("upload_id", ""),
            upload_id_str=data.get("upload_id_str", ""),
            external_id=data.get("external_id", ""),
            from_accepted_tag=data.get("from_accepted_tag", ""),
            pr_count=data.get("pr_count", ""),
            total_photo_count=data.get("total_photo_count", ""),
            has_kudoed=data.get("has_kudoed", ""),
        )
    
    def as_dict(self) -> dict:
        return dataclasses.asdict(self)
    
@dataclasses.dataclass
class DetailedRun:
    resource_state: int
    athlete: dict
    name: str
    distance: float
    moving_time: int
    elapsed_time: int
    total_elevation_gain: float
    type: str
    sport_type: str
    workout_type: int
    id: int
    start_date: str
    start_date_local: str
    timezone: str
    utc_offset: float
    location_city: str | None
    location_state: str | None
    location_country: str | None
    achievement_count: int
    kudos_count: int
    comment_count: int
    athlete_count: int
    photo_count: int
    map: dict
    trainer: bool
    commute: bool
    manual: bool
    private: bool
    visibility: str
    flagged: bool
    gear_id: str | None
    start_latlng: list
    end_latlng: list
    average_speed: float
    max_speed: float
    average_cadence: float
    average_temp: int
    average_watts: float
    max_watts: int
    weighted_average_watts: int
    device_watts: bool
    kilojoules: float
    has_heartrate: bool
    heartrate_opt_out: bool
    display_hide_heartrate_option: bool
    elev_high: float
    elev_low: float
    upload_id: int
    upload_id_str: str
    external_id: str
    from_accepted_tag: bool
    pr_count: int
    total_photo_count: int
    has_kudoed: bool
    description: str
    calories: float
    perceived_exertion: str | None
    prefer_perceived_exertion: str | None
    segment_efforts: list
    splits_metric: list
    splits_standard: list
    laps: list
    best_efforts: list
    photos: dict
    stats_visibility: list
    hide_from_home: bool
    device_name: str
    embed_token: str
    similar_activities: dict
    available_zones: list

    @staticmethod
    def from_dict(data: dict) -> "DetailedRun":
        return DetailedRun(
            resource_state=data.get('resource_state', ''),
            athlete=data.get('athlete', ''),
            name=data.get('name', ''),
            distance=data.get('distance', ''),
            moving_time=data.get('moving_time', ''),
            elapsed_time=data.get('elapsed_time', ''),
            total_elevation_gain=data.get('total_elevation_gain', ''),
            type=data.get('type', ''),
            sport_type=data.get('sport_type', ''),
            workout_type=data.get('workout_type', ''),
            id=data.get('id', ''),
            start_date=data.get('start_date', ''),
            start_date_local=data.get('start_date_local', ''),
            timezone=data.get('timezone', ''),
            utc_offset=data.get('utc_offset', ''),
            location_city=data.get('location_city', ''),
            location_state=data.get('location_state', ''),
            location_country=data.get('location_country', ''),
            achievement_count=data.get('achievement_count', ''),
            kudos_count=data.get('kudos_count', ''),
            comment_count=data.get('comment_count', ''),
            athlete_count=data.get('athlete_count', ''),
            photo_count=data.get('photo_count', ''),
            map=data.get('map', ''),
            trainer=data.get('trainer', ''),
            commute=data.get('commute', ''),
            manual=data.get('manual', ''),
            private=data.get('private', ''),
            visibility=data.get('visibility', ''),
            flagged=data.get('flagged', ''),
            gear_id=data.get('gear_id', ''),
            start_latlng=data.get('start_latlng', ''),
            end_latlng=data.get('end_latlng', ''),
            average_speed=data.get('average_speed', ''),
            max_speed=data.get('max_speed', ''),
            average_cadence=data.get('average_cadence', ''),
            average_temp=data.get('average_temp', ''),
            average_watts=data.get('average_watts', ''),
            max_watts=data.get('max_watts', ''),
            weighted_average_watts=data.get('weighted_average_watts', ''),
            device_watts=data.get('device_watts', ''),
            kilojoules=data.get('kilojoules', ''),
            has_heartrate=data.get('has_heartrate', ''),
            heartrate_opt_out=data.get('heartrate_opt_out', ''),
            display_hide_heartrate_option=data.get('display_hide_heartrate_option', ''),
            elev_high=data.get('elev_high', ''),
            elev_low=data.get('elev_low', ''),
            upload_id=data.get('upload_id', ''),
            upload_id_str=data.get('upload_id_str', ''),
            external_id=data.get('external_id', ''),
            from_accepted_tag=data.get('from_accepted_tag', ''),
            pr_count=data.get('pr_count', ''),
            total_photo_count=data.get('total_photo_count', ''),
            has_kudoed=data.get('has_kudoed', ''),
            description=data.get('description', ''),
            calories=data.get('calories', ''),
            perceived_exertion=data.get('perceived_exertion', ''),
            prefer_perceived_exertion=data.get('prefer_perceived_exertion', ''),
            segment_efforts=data.get('segment_efforts', ''),
            splits_metric=data.get('splits_metric', ''),
            splits_standard=data.get('splits_standard', ''),
            laps=data.get('laps', ''),
            best_efforts=data.get('best_efforts', ''),
            photos=data.get('photos', ''),
            stats_visibility=data.get('stats_visibility', ''),
            hide_from_home=data.get('hide_from_home', ''),
            device_name=data.get('device_name', ''),
            embed_token=data.get('embed_token', ''),
            similar_activities=data.get('similar_activities', ''),
            available_zones=data.get('available_zones', ''),
        )
    
    def as_dict(self) -> dict:
        return dataclasses.asdict(self)
    
