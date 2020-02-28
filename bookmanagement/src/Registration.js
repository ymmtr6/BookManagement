import React from "react";

class Registration extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      usstate: props.initState,
      desc: "This is for a text area."
    };

    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
    this.onTextAreaChange = this.onTextAreaChange.bind(this);
  }

  onChange(e) {
    this.setState({ usstate: e.target.value });
  }

  onSubmit(e) {
    e.preventDefault();
  }

  onTextAreaChange(e) {
    this.setState({ desc: e.target.value });
  }


  render() {
    return (
      <div>
        <span>Test</span>
        <form onSubmit={this.onSubmit}>
          <textarea
            value={this.state.desc}
            onChange={this.onTextAreaChange} />
          <div>
            <button type="submit">OK</button>
          </div>
        </form>
      </div>
    )
  }

}

export default Registration;
