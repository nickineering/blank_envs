import { useQuery } from "@tanstack/react-query";

export function useSources() {
  return useQuery({
    queryKey: ["sourcesData"],
    queryFn: () =>
      fetch("http://localhost:3000/sources/1").then((res) => res.json()),
  });
}
