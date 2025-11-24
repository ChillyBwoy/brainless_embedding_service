from fastapi import APIRouter
from transformers import AutoModelForCausalLM, AutoTokenizer

from core.config import get_settings
from schemas.message import Message

router = APIRouter(tags=["predictions"])

settings = get_settings()


@router.post("/predict", response_model=Message)
async def predict(message: Message):
    tokenizer = AutoTokenizer.from_pretrained(
        settings.prediction_model_name,
        cache_dir=settings.cache_folder,
        token=settings.hf_token,
    )

    model = AutoModelForCausalLM.from_pretrained(
        settings.prediction_model_name,
        cache_dir=settings.cache_folder,
        token=settings.hf_token,
    )
    inputs = tokenizer(message.content, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs)
    text = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return Message(content="\n".join(text))
