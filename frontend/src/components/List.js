import "./List.css";

const List = ({urls, visibility}) => {

  return (
    
    <div className="list-wrapper" style={{display: visibility ? 'flex' : 'none' }}>
      {
        urls.map((url) => (
          <div className="listCard">
            <p><span>Short Link:</span>{url.shortlink}</p>
            <p><span>Url: </span>{url.url}</p>
          </div>
        ))
      }
    </div>
  );
};

export default List;

