import React, {useState} from 'react'
import Form from './Form';
import HistoryList from './HistoryList';

function App() {

  const [display, setDisplay] = useState('Form')

  const handleDisplay = (component_name) => {
    setDisplay(component_name)
  }

    return (
      <div className='container'>
        { display === 'Form' && ( 
          <>
            <button onClick={ () => handleDisplay('HistoryList') } className='switch'>
              履歴一覧画面へ
            </button>
            <Form />
          </>
        )}
        { display === 'HistoryList' && ( 
          <>
            <button onClick={ () => handleDisplay('Form') } className='switch'>
              Botとの会話画面へ
            </button>
            <HistoryList />
          </>
        )}
      </div>
    )
}

export default App;
