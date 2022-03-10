import React from 'react';

class Form extends React.Component {
  render() {
    return (
      <div className='form'>
        <form>
          <input />
          <input
            type='submit'
            value='送信'
          />
        </form>
      </div>
    );
  }
}

export default Form;
