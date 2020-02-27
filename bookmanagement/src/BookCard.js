import React from "react";
import Modal from "react-modal";

Modal.setAppElement("#root");

// modal css json
const modalStyles = {
  overlay: {
    position: "fixed",
    top: 50,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: "rgba(255, 255, 255, 0.75)"
  },
  content: {
    width: "80%",
    height: "80%",
    posiiton: "absolute",
    left: "50%",
    top: "50%",
    transform: "translate(-50%, -50%)"
  }
};

class Books extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      target: [],
      modalIsOpen: false
    };
  }

  openModal(book) {
    this.setState({
      target: book,
      modalIsOpen: true
    });
  }

  closeModal() {
    this.setState({
      target: [],
      modalIsOpen: false
    });
  }

  renderProducts(product) {
    return (
      //  {_id, authors, description, isbn, publishedDate, registered, thumbnail, title}). If you meant to render a collection of children, use an array instead.
      <div className="">
        <div>
          <svg className="float-right fill-current text-black" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" onClick={this.closeModal.bind(this)}>
            <path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
          </svg>
        </div>
        <div className="flex justify-center">
          <img src={product.thumbnail} alt={product.title} className="w-1/3 h-1/2" />

        </div>
        <div className="table">
          <div className="table-row">
            <div className="table-cell">Title</div>
            <div className="table-cell">{product.title}</div>
          </div>
          <div className="table-row">
            <div className="table-cell">Authors</div>
            <div className="table-cell">{"authors" in product ? product.authors.join(", ") : ""}</div>
          </div>
          <div className="table-row">
            <div className="table-cell">ISBN</div>
            <div className="table-cell">{product.isbn}</div>
          </div>
          <div className="table-row">
            <div className="table-cell">Publisher</div>
            <div className="table-cell">{product.publisher}</div>
          </div>
          <div className="table-row">
            <div className="table-cell">PublishedDate</div>
            <div className="table-cell">{product.publishedDate}</div>
          </div>
          <div className="table-row">
            <div className="table-cell">Registered</div>
            <div className="table-cell">{product.registered}</div>
          </div>
          <div className="table-row">
            <div className="table-cell">Description</div>
            <div className="table-cell">{product.description}</div>
          </div>
        </div>
        <div className="flex justify-center">
          <button onClick={this.closeModal.bind(this)}>Close</button>
        </div>
      </div>
    )
  }

  render() {
    return (
      <div>
        <div className="flex mb-4 justify-center items-center flex-wrap" id="CardView">{
          this.props.books.map((book, index) => (
            <div className="p-4 hvr-grow" onClick={this.openModal.bind(this, book)} key={book.isbn}>
              <div className="max-w-sm rounded overflow-hidden shadow-lg text-center">
                <img
                  className="h-1/2 w-32 sm:w-32 md:w-64 lg:w-64 xl:w-64 mx-auto"
                  src={"thumbnail" in book ? (book.thumbnail) : "./img/noimage.png"}
                  alt="book thumnail"
                ></img>
                <div className="px-6 py-4">
                  <div className="font-bold text-base sm:text-base md:text-xl lg:text-xl mb-2 w-32 sm:w-32 md:w-64 lg:w-64 xl:w-64">{book.title}</div>
                  <p className="text-gray-700 text-sm sm:text-sm md:text-base lg:text-base w-32 sm:w-32 md:w-64 lg:w-64 xl:w-64">
                    {"authors" in product ? product.authors.join(", ") : ""}
                  </p>
                </div>
              </div>
            </div>
          ))
        }
        </div>
        <Modal isOpen={this.state.modalIsOpen} onRequestClose={this.closeModal.bind(this)} style={modalStyles} contentLabel="Example Modal">
          {this.renderProducts(this.state.target)}
        </Modal>
      </div >
    )
  }
}

export default Books

/*
<ContentCard
      pageName={book.title}
      imgSrc={"thumbnail" in book ? (book.thumbnail) : "./img/noimage.png"}
      discription={book.authors instanceof Array ? book.authors.join(" ") : book.authors}
      key={book.isbn}
      onClick={this.openModal.bind(this, book)}
    />
    */
