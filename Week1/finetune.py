from transformers import Trainer, TrainingArguments

training_args = TrainingArguments("test_trainer")

trainer = Trainer(
    model=None,
    args=training_args,
    train_dataset=None,
    eval_dataset=None,
)

trainer.train()