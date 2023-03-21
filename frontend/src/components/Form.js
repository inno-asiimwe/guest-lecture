import { useState, useRef, useEffect } from "react";
import axios from 'axios'
import "./Form.css";

const apiHost = process.env.REACT_APP_API_HOST

const Form = ({setUrls, setvisibility, visibility}) => {
  const urlInput = useRef(null);
  const shortUrl = useRef(null);
  const [shortenedUrl, setShortenedUrl] = useState(null);
  const [error, setError] = useState(null);

  const makeShortendUrl = (event) => {
    event.preventDefault();
    const inputUrl = urlInput.current.value;

    if (!inputUrl.length) {
      setError("Please input valid url");
      return;
    }

    axios.post(`${apiHost}/api/v1/shorturl`, {url: inputUrl}).then(response => {
      setShortenedUrl(response.data.data.shortlink)
    }).catch(error => {
      setError(error.response.data.message)
    })

  };

  const copyUrl = (event) => {
    event.preventDefault();
    const target = shortUrl.current;
    target.select();
    document.execCommand("copy");
  };

  const getUrls = () => {
    setvisibility(!visibility)
    axios.get(`${apiHost}/api/v1/shorturl`).then(response => {
      setUrls("")
      setUrls(response.data.data)
    }).catch(error => {
      setError(error.response.data.message)
    })
  }

  const resetForm = () => {
    setShortenedUrl(null)
    setUrls("")

  }

  return (
    <div className="form-wrapper form--white">
      <div className="card">
        {error && <p className="error">Error: {error}</p>}
        <div className="mb-3">
          <label className="label-input">
            Enter long URL to shorten
          </label>
          <input
            id="shorturl"
            className="control-input"
            name="shorturl"
            ref={urlInput}
          />
        </div>
        {shortenedUrl && (
          <div className="mb-3">
            <label className="label-input">ShortLink</label>
            <input
              id="shorturl-shortened"
              value={shortenedUrl}
              ref={shortUrl}
              className="control-input control-input-url"
              readOnly
            />
          </div>
        )}

        {shortenedUrl && (
          <div className="mt-10">
            <a target="_blank" href={shortenedUrl}>
              <button className="toolbar-btn clr-bg-blue">Visit</button>
            </a>
            <a target="_blank" className="ml-5">
              <button className="toolbar-btn clr-bg-green" onClick={copyUrl}>
                Copy
              </button>
            </a>
          </div>
        )}

        {!shortenedUrl && (
          <div className="mt-10 btn-wrapper">
            <button className="form-btn" onClick={makeShortendUrl}>
              Shorten URL
            </button>
          </div>
        )}

        {shortenedUrl && (
          <div className="mt-10 btn-wrapper">
            <button onClick={getUrls} className="form-btn clr-bg-white wd-30">URLs</button>
            <button onClick={resetForm} className="form-btn clr-bg-green wd-70 ml-5">
              Shorten another
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default Form;
