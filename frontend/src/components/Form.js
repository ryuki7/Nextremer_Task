import React, {useState} from 'react'
import axios from 'axios'
import TalkIndex from './TalkIndex';

function Form() {

  const [formData, setFormData] = useState({
    user_input: "",
  })

  const [talkDatas, setTalkDatas] = useState([])

  const [send_currentTime, setSendCurrentTime] = useState([])

  const CurrentTimeRecord = () => {
    setSendCurrentTime([ ...send_currentTime, new Date().toLocaleTimeString() ])
  }

  const handleFormSubmit = (event) => {
    event.preventDefault();
    CurrentTimeRecord();
    setFormData({
      user_input: ""
    })
    axios.post('http://127.0.0.1:5000/chat', {
      formData
    })
    .then(res => {
      setTalkDatas([ ...talkDatas, res.data ])
      console.log(talkDatas)
      console.log(send_currentTime)
    })
    .catch(() => {
      console.log('通信に失敗しました');
    });
  }

  const handleTalkInputChange = event => {
    const inputValue = event.target.value;

    setFormData({
      user_input: inputValue
    })
  }

    return (
      <div className='form_and_talk'>
        <div className='form'>
          <form onSubmit={ event => handleFormSubmit(event) }>
            <input
              value={ formData.user_input }
              onChange={ event => handleTalkInputChange(event) }
            />
            <button type="submit">
              送信
            </button>
          </form>
        </div>

        <TalkIndex
          talk_data_array={ talkDatas }
          send_current_time_array={ send_currentTime }
        />

      </div>
    );
};

export default Form;
