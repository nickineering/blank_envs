import { useMutation } from "@tanstack/react-query";
import { useSources } from "../queries/useSources";

export function Sources() {
  const { isPending, error, data } = useSources();
  // const [text, setText] = useState();

  const mutation = useMutation({
    mutationFn: (data) => {
      return fetch("http://localhost:3000/comments/", {
        method: "post",
        body: JSON.stringify(data),
        headers: { "Content-Type": "application/json" },
      }).then((res) => res.json());
    },
  });

  if (isPending)
    return <button aria-busy="true" className="secondary"></button>;

  if (error) return <article>An error has occurred {error.message}</article>;

  const translations = [];
  for (const translation of data.translations) {
    translations.push(<li>{translation.text}</li>);
  }

  const comments = [];
  for (const comment of data.comments) {
    translations.push(<li>{comment.text}</li>);
  }

  const submitComment = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    mutation.mutate({ sourceId: 1, text: formData.get("text") });
  };

  return (
    <div>
      <h1>{data.text}</h1>
      <ul>{translations}</ul>
      <ul>{comments}</ul>

      {mutation.isPending ? (
        <p>Submitting</p>
      ) : (
        <>
          {mutation.isError ? (
            <div>An error occurred: {mutation.error.message}</div>
          ) : null}

          {mutation.isSuccess ? <div>Comment added!</div> : null}
        </>
      )}

      <form onSubmit={submitComment}>
        <input type="text" name="text"></input>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
