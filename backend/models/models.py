from database import db

class Chatbot(db.Model):
    __tablename__ = 'chatbots'
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(255))
    bot_response = db.Column(db.String(255))
    response_timestamp = db.Column(db.String(255), nullable=False)

    def toDict(self):
        return {
            'user_input': self.user_input,
            'bot_response': self.bot_response,
            'response_timestamp': self.response_timestamp
        }