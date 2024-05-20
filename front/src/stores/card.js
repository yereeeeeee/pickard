import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useCardStore = defineStore('card', () => {
  const cards = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  const brands = ['BC카드', '부산은행', '대구은행', '기업은행', '국민카드', '농협카드']

  const readCard = function () {
    axios({
      method: 'get',
      url: `${API_URL}/cards/`,
    })
    .then(res => {
      cards.value = res.data
    })
    .catch(err => console.error(err))
  }
  
  const benefit_dict = ref({
    "간편결제": 0,
    "공과금/렌탈": 1,
    "공항라운지/PP": 2,
    "교육/육아": 3,
    "교통": 4,
    "레저/스포츠": 5,
    "마트/편의점": 6,
    "배달앱": 7,
    "병원/약국": 8,
    "뷰티/피트니스": 9,
    "쇼핑": 10,
    "애완동물": 11,
    "여행/숙박": 12,
    "영화/문화": 13,
    "자동차/하이패스": 14,
    "주유": 15,
    "카페/디저트": 16,
    "통신": 17,
    "푸드": 18,
    "항공마일리지": 19,
    "항공": 20,
    "해외": 21,
})

  return {
    cards, brands, API_URL, benefit_dict,
    readCard,
  }

})
