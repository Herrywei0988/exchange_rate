from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
import pandas as pd

class ExchangeRateRecord(BaseModel):
    base: str
    target: str
    rate: float = Field(..., gt=0)
    timestamp: int

    def to_dict(self):
        return {
            "base": self.base,
            "target": self.target,
            "rate": self.rate,
            "timestamp": datetime.utcfromtimestamp(self.timestamp).strftime('%Y-%m-%d')
        }

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    validated = []

    for _, row in df.iterrows():
        try:
            record = ExchangeRateRecord(
                base=row["base"],
                target=row["target"],
                rate=row["rate"],
                timestamp=row["timestamp"]
            )
            validated.append(record.to_dict())
        except ValidationError as e:
            print(f"[Validation Error] Skipped row: {e}")

    return pd.DataFrame(validated)
