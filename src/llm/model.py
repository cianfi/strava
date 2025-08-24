import dataclasses

@dataclasses.dataclass
class LLMResponse:
    response: str

    @staticmethod
    def from_dict(data: dict) -> "LLMResponse":
        return LLMResponse(
            response=data.get("response", "")
        )
    
    @staticmethod
    def from_str(data: str) -> "LLMResponse":
        return LLMResponse(
            response=data
        )

    def as_dict(self) -> dict:
        return dataclasses.asdict(self)
    
