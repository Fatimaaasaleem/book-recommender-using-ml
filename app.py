from flask import Flask, render_template, request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=list(popular_df['avg_ratings'].values)
    )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    #we will make a function named recommen , jis ke input mein book ka naam hoga aur wo return mein mujhe 5 recommendatiosn dega
    index=np.where(pt.index==user_input)[0][0]#locating index of the book
    similar_items=sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
    #what this statement does is it will find the similairty socre of the book with the rest of it, will give us a sorted list with greater scores at the top, why i used lambda here is cuz it sorted on the based of index, i wanted it to sort on the basis of next thing, which were scores, then i only kept the first six books greatest similairity score
    data=[]
    for i in similar_items:
        item=[]
        print(pt.index[i[0]])
        temp_df=books[books['Book-Title']==pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        
        data.append(item)  
    # the zero here s for index, it will give index and names of books    
    print(data)
    return render_template('recommend.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
