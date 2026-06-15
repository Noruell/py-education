from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI(title="TODO-лист API")

# ========== МОДЕЛИ ==========
class Task(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TaskOut(Task):
    id: int

# ========== ХРАНИЛИЩЕ ==========
tasks_db = []
task_id_counter = 1

# ========== ЭНДПОИНТЫ ==========
@app.get("/", response_class=HTMLResponse)
def main_page():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/tasks", response_model=List[TaskOut])
def get_all_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=TaskOut, status_code=201)
def create_task(task: Task):
    global task_id_counter
    new_task = task.model_dump()
    new_task["id"] = task_id_counter
    task_id_counter += 1
    tasks_db.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task: Task):
    for i, existing_task in enumerate(tasks_db):
        if existing_task["id"] == task_id:
            updated_task = task.model_dump()
            updated_task["id"] = task_id
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db.pop(i)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")