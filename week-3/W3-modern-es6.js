const loadingSpinnerAdjacentHTML = `
<div
  id="loading-spinner"
  class="wrapper">
    <div class="loadingSpinner">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
</div>
`;

/**
 * sleep
 * 等於 python 中的 time.sleep()
 * @param {Number} ms 毫秒
 * @returns 
 */
function sleep(ms = 0) {
  return new Promise((res) => setTimeout(res, ms));
}

/**
 * 此情境，http request 只需發一次，完全沒有必要發 8 次相同的 http request;
 * 發一次，並且用變數存起來就好了
 */
async function getSrcByAjaxRequest(uri = '', ms = 0) {
  await sleep(ms);
  return fetch(uri).then(response => response.json());
}

async function main() {
    /** 因為 ajax request 還沒得到回應，先顯示 loading spinner */
    document.body.insertAdjacentHTML('beforeend', loadingSpinnerAdjacentHTML);

    // 進行 ajax request 取得 image src 
    const response = await getSrcByAjaxRequest(
      'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json',
      5000, // 這邊為了展示非同步執行，讓執行緒睡 5 秒
    );

    // 確定得到 response 後 移除 loading spinner
    document.body.removeChild(document.getElementById('loading-spinner'));

    // 然後插入 content
    const content = document.createElement('div');
    document.body.appendChild(content);
    content.setAttribute("class", "content");

    // modern js 請用 es6 來處理 for loop
    // 開發上很少機會使用到原生 for (let i = 0; .....)，會很醜
    Array.from(Array(8)).forEach((_, index) => {
        /**
         * all section
         */
        const all = document.createElement('div');
        content.appendChild(all);
        all.setAttribute("class", "all");
    
        /**
         * img section
         */
        const myString = response.result.results[index].file;
        const splits = myString.split(['https']);
        const src = `https${splits[1]}`;
        const img = document.createElement('img');
        all.appendChild(img);
        img.setAttribute("src", src);
        img.setAttribute("class", "img");
    
        /**
         * name section
         */
        const name = document.createElement('div');
        all.appendChild(name);
        name.textContent = response.result.results[index].stitle;
        name.setAttribute("class", "img_name");
    })   
}

main();