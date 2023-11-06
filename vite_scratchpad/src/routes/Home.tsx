import { useRepo } from "../queries/useRepo";

export function Home() {
  const { isPending, error, data } = useRepo();

  if (isPending)
    return <button aria-busy="true" className="secondary"></button>;

  if (error) return <article>An error has occurred {error.message}</article>;

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.description}</p>
      <strong>👀 {data.subscribers_count}</strong>{" "}
      <strong>✨ {data.stargazers_count}</strong>{" "}
      <strong>🍴 {data.forks_count}</strong>
    </div>
  );
}
