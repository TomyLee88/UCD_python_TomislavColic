from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
blog_posts = {
    'post_1': {
        'title': 'Exploring the Amazon Rainforest',
        'content': 'Embark on a mesmerizing journey through the vast Amazon rainforest, a sanctuary for biodiversity. '
                   'Discover the wonders of the world\'s largest tropical rainforest, and learn about its unique ecosystems and the importance of conservation.',
        'author': 'John Doe',
        'date': '2023-10-10',
        'category': 'Nature',
    },
    'post_2': {
        'title': 'The Quantum World Unveiled',
        'content': 'Dive deep into the fascinating realm of quantum physics, where particles defy classical physics laws. '
                   'Explore the mysteries of superposition, entanglement, and quantum computing, and grasp the profound implications of quantum mechanics.',
        'author': 'Jane Smith',
        'date': '2023-10-12',
        'category': 'Science',
    },
    'post_3': {
        'title': 'Global Headlines: What You Need to Know',
        'content': 'Stay informed about the latest global events and developments. Our dedicated news team provides comprehensive coverage of critical issues in politics, technology, and more.',
        'author': 'Alexandra Williams',
        'date': '2023-10-20',
        'category': 'News',
    },
    'post_4': {
        'title': 'Master the Art of Gourmet Cooking',
        'content': 'Elevate your culinary skills to new heights with expert cooking tips and a treasure trove of mouthwatering recipes. '
                   'From classic dishes to innovative creations, discover the art of gourmet cooking and impress your guests.',
        'author': 'Michael Johnson',
        'date': '2023-10-25',
        'category': 'Cooking',
    },
    'post_5': {
        'title': 'Adventures in Patagonia: Nature\'s Playground',
        'content': 'Embark on a thrilling adventure through the awe-inspiring landscapes of Patagonia. '
                   'Trek through pristine forests, witness the grandeur of glaciers, and experience the untouched beauty of this remote region.',
        'author': 'Sophia Roberts',
        'date': '2023-10-30',
        'category': 'Travel',
    },
    'post_6': {
        'title': 'The Universe: A Cosmic Odyssey',
        'content': 'Journey through the cosmos and explore the remarkable achievements of space exploration. '
                   'From moon landings to the search for extraterrestrial life, space remains an unending source of wonder and discovery.',
        'author': 'David Clark',
        'date': '2023-11-02',
        'category': 'Science',
    },
    'post_7': {
        'title': 'Your Path to Holistic Health and Wellness',
        'content': 'Discover the keys to a healthier lifestyle, encompassing nutrition, fitness, and mental well-being. '
                   'Embark on your journey to improved health, vitality, and overall well-being through mindful living.',
        'author': 'Olivia Davis',
        'date': '2023-11-05',
        'category': 'Health',
    },
    'post_8': {
        'title': 'Sustainable Gardening: A Greener Future',
        'content': 'Learn how to create a sustainable garden that benefits the environment and nurtures your well-being. '
                   'Explore eco-friendly gardening practices, grow your organic produce, and embrace sustainable living.',
        'author': 'William Green',
        'date': '2023-11-08',
        'category': 'Nature',
    }
}
@app.route('/category/<string:category>')
def list_posts_by_category(category):
    category_posts = {post_sku: post for post_sku, post in blog_posts.items() if post.get('category') == category}
    return render_template("list_posts_by_category.html", category=category, posts=category_posts)
@app.route('/')
def home():
    categories = set(post['category'] for post in blog_posts.values())
    return render_template("index.html", categories=categories, posts=blog_posts)
@app.route('/blog')
def list_blog_posts():
    return render_template("list_blog_posts.html", posts=blog_posts)
@app.route('/blog_view/<string:post_sku>')
def view_blog_post(post_sku):
    post = blog_posts.get(post_sku)
    if post:
        return render_template("view_blog_post.html", post=post)
    else:
        return "Blog post not found", 404
@app.route('/admin')
def admin_interface():
    return render_template('admin_interface.html', blog_posts=blog_posts)
@app.route('/admin/create_blog_post', methods=['GET', 'POST'])
def create_blog_post_form():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        date = request.form.get('date')
        category = request.form.get('category')
        # This small code to found all posts and add was pain
        existing_post_ids = [int(post_id.split('_')[1]) for post_id in blog_posts.keys()]
        new_post_id = f'post_{max(existing_post_ids) + 1}'
        # Pain end here
        blog_posts[new_post_id] = {
            'title': title,
            'content': content,
            'author': author,
            'date': date,
            'category': category
        }
        return redirect(url_for('admin_interface'))
    return render_template('create_blog_post_form.html')

@app.route('/delete/<string:post_id>', methods=['GET', 'POST'])
def delete_blog_post_form(post_id):
    if post_id in blog_posts:
        del blog_posts[post_id]
        return redirect(url_for('admin_interface'))
    else:
        return "Blog post not found", 404
if __name__ == '__main__':
    app.run(debug=True, port=5000)