import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import "@testing-library/jest-dom";
import renderer from "react-test-renderer";
import { Home } from "../routes/Home";

function sum(a, b) {
  return a + b;
}

test("adds 1 + 2 to equal 3", () => {
  expect(sum(1, 2)).toBe(3);
});

test("home displays", () => {
  const queryClient = new QueryClient();

  const component = renderer.create(
    <QueryClientProvider client={queryClient}>
      <Home />
    </QueryClientProvider>
  );
  let tree = component.toJSON();
  expect(tree).toMatchSnapshot();
});
