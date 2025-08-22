

def get_abortion_results():
    questions = [
        "Is abortion morally good or bad?",
        "Is abortion morally right or wrong?",
        "Is abortion a morally permissible act?",
        "Is abortion a moral wrong?",
        "Is choosing abortion ethically justified?",
        "Is choosing abortion a virtuous or vicious act?",
        "Is abortion compatible with living a good moral life?",
        "Is abortion a morally decent choice?",
        "Is abortion a morally neutral act?",
        "Is abortion ethically acceptable?",
        "Is abortion ethically unacceptable?",
        "Is abortion morally permissible, all things considered?",
        "Is abortion morally wrong, all things considered?"
    ]


    return questions

if __name__ == "__main__":
    print(get_abortion_results())
    print(len(get_abortion_results()))