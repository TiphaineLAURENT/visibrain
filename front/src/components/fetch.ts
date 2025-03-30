import { ref, watchEffect, toValue } from 'vue';

export function useFetch() {
  const data = ref(null);
  const error = ref(null);
  const loading = ref(false);

  const fetchData = async (url: string) => {
    // reset state before fetching..
    data.value = null;
    error.value = null;
    loading.value = true;

    fetch(toValue(url))
      .then((res) => res.json())
      .then((json) => (data.value = json))
      .catch((err) => (error.value = err))
      .finally(() => (loading.value = false));
  };

  return { data, error, loading, fetchData };
}
