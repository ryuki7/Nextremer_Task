import React from 'react'

function TalkIndex(props) {
    const TalkDataDivArray = props.talk_data_array.map( (talk_data, index) => 
      <div key={ 'each_talk_' + String(index) } className='each_talk_set'>
        <p>{ props.send_current_time_array[index] + ' You > ' + talk_data.user_input }</p>
        <p>{ talk_data.response_timestamp + ' Bot > ' + talk_data.bot_response }</p>
      </div>
    )

    return (
      <div className='talk_index'>
        { TalkDataDivArray }
      </div>
    );
};

export default TalkIndex;
