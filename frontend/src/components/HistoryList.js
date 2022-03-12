import React, {useState, useEffect} from 'react'
import axios from 'axios'

function HistoryList() {

  const [talkDataArray, setTalkDataArray] = useState([])

  // ブラウザでこのコンポーネントが表示される時に1度だけ実行される。（第2引数に[]を指定している為。）
  useEffect(()=>{
    axios.get('http://127.0.0.1:5000/history/list')
    .then(res => {
      setTalkDataArray(res.data)
      // console.log(res.data)
    })
    .catch(() => {
      console.log('通信に失敗しました');
    });
  }, [])

  const TalkDataTrArray = talkDataArray.map( (talk_data, index) => 
      <tr key={ 'each_history_' + String(index) }>
        <td>{ talk_data.user_input }</td>
        <td>{ talk_data.bot_response }</td>
        <td>{ talk_data.response_timestamp }</td>
      </tr>
    )

    return (
      <table className='history_list'>
        <tbody>
          <tr>
            <th>自分の入力</th>
            <th>Botの応答</th>
            <th>Botの応答時刻</th>
          </tr>
          { TalkDataTrArray }
        </tbody>
      </table>
    );
};

export default HistoryList;
