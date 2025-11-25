from fastapi import APIRouter, Depends
from transformers import PreTrainedTokenizer, PreTrainedModel
from typing import Annotated

from app.dependencies import get_tokenizer, get_prediction_model
from app.schemas import Message, Prompt

router = APIRouter(tags=["predictions"])


@router.post("/predict", response_model=Message)
async def predict(
    prompt: Prompt,
    tokenizer: Annotated[PreTrainedTokenizer, Depends(get_tokenizer)],
    model: Annotated[PreTrainedModel, Depends(get_prediction_model)],
):
    messages = [{"role": "user", "content": prompt.content}]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=True,
    )

    model_inputs = tokenizer(text, return_tensors="pt").to(model.device)  # type: ignore
    generated_ids = model.generate(**model_inputs)  # type: ignore

    print(generated_ids)

    output_ids = generated_ids[0][len(model_inputs.input_ids[0]) :].tolist()

    # parsing thinking content
    try:
        # rindex finding 151668 (</think>)
        index = len(output_ids) - output_ids[::-1].index(151668)
    except ValueError:
        index = 0

    thinking_content = tokenizer.decode(
        output_ids[:index], skip_special_tokens=True
    ).strip("\n")
    content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

    return Message(content=content, thinking=thinking_content)
