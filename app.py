from flask  import Flask, request, redirect, render_template, session, flash, url_for
from models import dbConnect
from util.user import User
from datetime import timedelta
import hashlib
import uuid
import re


app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=30)


@app.route('/signup')
def signup():
    return render_template('registration/signup.html')


@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if name == '' or email == '' or password1 == '' or password2 == '':
        flash('入力されていないところがあります。')
    elif password1 != password2:
        flash('２つのパスワードが一致していません。')
    elif re.match(pattern, email) is None:
        flash('メールアドレスの形式が正しくありません。')
    else:
        id = uuid.uuid4()
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        user = User(id, name, email, password)
        DBuserEmail = dbConnect.getUser(email)
        DBuserId = dbConnect.getUserId(name)

        if DBuserId != None:
            flash("他のユーザーが使用している名前です。")
        elif DBuserEmail != None:
            flash('既に登録されたEmailアドレスです。')
        else:
            dbConnect.createUser(user)
            UserId = str(id)
            session['uid'] = UserId
            return redirect('/')
    return redirect('/signup')


@app.route('/login')
def login():
    return render_template('registration/login.html')


@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')

    if email =='' or password == '':
        flash('入力されていないところがあります。')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません。')
        else:
            hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hashPassword != user["password"]:
                flash('パスワードがちがいます。')
            else:
                session['uid'] = user['id']
                return redirect('/')
    return redirect('/login')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/')
def index():
    uid = session.get("uid")
    if uid is None:
        return render_template('top.html')
    else:
        channels = dbConnect.getChannelAll()

    return render_template('index.html', channels=channels, uid=uid)


@app.route('/', methods=['POST'])
def add_channel():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    channel_name = request.form.get('channel-title')
    channel = dbConnect.getChannelByName(channel_name)
    if channel == None:
        channel_description = request.form.get('channel-description')
        dbConnect.addChannel(uid, channel_name, channel_description)
        return redirect('/')
    else:
        error = '同じ名前のチャンネルが存在します。'
        return render_template('error/error.html', error_message=error)


@app.route('/update_channel', methods=['POST'])
def update_channel():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    cid = request.form.get('cid')
    channel_name = request.form.get('channel-title')
    channel_description = request.form.get('channel-description')

    dbConnect.updateChannel(uid, channel_name, channel_description, cid)
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    reactions = dbConnect.getReactionAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, reactions=reactions)


@app.route('/delete/<cid>')
def delete_channel(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        channel =dbConnect.getChannelById(cid)
        if channel["uid"] != uid:
            flash('チャンネルは作成者のみ削除可能です。')
            return redirect('/')
        else:
            dbConnect.deleteChannel(cid)
            channels = dbConnect.getChannelAll()
            return render_template('index.html', channels=channels, uid=uid)



@app.route('/detail/<cid>')
def detail(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = cid
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    reactions = dbConnect.getReactionAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid, reactions=reactions)


@app.route('/message', methods=['POST'])
def add_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    
    message = request.form.get('message')
    channel_id =request.form.get('channel_id')

    if message.strip():
        dbConnect.createMessage(uid, channel_id, message)
 
    return redirect(url_for('message_result', channel_id=channel_id))

@app.route('/message_result/<channel_id>')
def message_result(channel_id):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    
    channel = dbConnect.getChannelById(channel_id)
    messages = dbConnect.getMessageAll(channel_id)
    reactions = dbConnect.getReactionAll(channel_id)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid, reactions=reactions)

@app.route('/reaction', methods=['POST'])
def reaction():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    
    mid = request.form.get('message_id')
    reaction_code = request.form.get('reaction_code')
    channel_id =request.form.get('channel_id')
    try:
        dbConnect.addReaction(mid, uid, reaction_code)
        return redirect(url_for('result', channel_id=channel_id))
    except:
        return redirect(url_for('result', channel_id=channel_id))



@app.route('/delete_message', methods=['POST'])
def delete_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    mid = request.form.get('message_id')
    cid = request.form.get('channel_id')
    if mid:
        dbConnect.deleteMessage(mid)

    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    reactions = dbConnect.getReactionAll(cid)
    
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, reactions=reactions)

@app.route('/result/<channel_id>')
def result(channel_id):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    
    channel = dbConnect.getChannelById(channel_id)
    messages = dbConnect.getMessageAll(channel_id)
    reactions = dbConnect.getReactionAll(channel_id)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid, reactions=reactions)

@app.route('/search', methods=['POST'])
def search():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    
    keyword = request.form.get('keyword')
    if keyword.strip():
        search_C_name, search_message = dbConnect.searchMessages(keyword)
        channels = dbConnect.getChannelAll()
        print(search_C_name, search_message)
        return render_template('index.html', channels=channels, uid=uid, search_C_name=search_C_name, search_message=search_message)
    else:
        channels = dbConnect.getChannelAll()
        return render_template('index.html', channels=channels, uid=uid)



@app.errorhandler(404)
def show_error404(error):
    return render_template('error/404.html')


@app.errorhandler(500)
def show_error500(error):
    return render_template('error/500.html')


if __name__ == '__main__':
    app.run(debug=True)
