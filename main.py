from flask import Flask, render_template, request, redirect
from helper_functions import get_all_tasks, insert_task, delete_task, clear_all_tasks, update_status, create_table

create_table()

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        task = request.form["task"]
        insert_task(task)
        return redirect("/")
    status = request.args.get('status',None)
    tasks = get_all_tasks(status)
    return render_template('index.html',tasks=tasks,size=len(tasks))
    
@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task(task_id)
    return redirect("/")

@app.route("/clear")
def clear():
    clear_all_tasks()
    return redirect("/")

@app.route("/update/<int:task_id>/<int:completed>")
def update(task_id,completed):
    status = None
    if completed == 1:
        status = 'completed'
    else:
        status = 'pending'
    update_status(task_id, status)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

