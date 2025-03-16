<template>
  <div class="card template-invoice-card mb-0">
    <div class="card-body pb-0">
      <div class="invoice-card-title">
        <h6>Receipt</h6>
      </div>
      <div class="row">
        <!-- Invoice List -->
        <div class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block" v-for="(image, index) in galleryImages" :key="index"
          @click="() => show(index)">
          <div
            class="blog grid-blog invoice-blog flex-fill d-flex flex-wrap align-content-betweens active"
          >
            <div class="blog-image">
              <a href="javascript:;" class="img-general"
                ><img
                  class="img-fluid"
                  :src="require(`@/assets/img/${image.img}`)"
                  alt="Post Image"
                />
              </a>
              <a
              :src="require(`@/assets/img/invoices/${image.src}`)"
                class="preview-invoice image-popup"
                ><i class="fa-regular fa-eye"></i
              ></a>
            </div>
            <div class="invoice-content-title">
              <a href="javascript:;">{{image.title}}</a>
              <span
                class="invoice-star"
                data-bs-toggle="tooltip"
                data-bs-placement="left"
                title=""
                data-bs-original-title="Make as default"
                ><i class="fa-regular fa-star"></i
              ></span>
            </div>
          </div>
        </div>
        <!-- /Invoice List -->
      </div>
    </div>
  </div>

  <vue-easy-lightbox :visible="visible" :index="index" :imgs="galleryImages.map((image) => ({
    src: require(`@/assets/img/invoices/${image.src}`),
  }))" @hide="visible = false" @on-prev="handlePrev" @on-next="handleNext">
  </vue-easy-lightbox>
</template>

<script>
import VueEasyLightbox from "vue-easy-lightbox";
export default {
  components: {
    VueEasyLightbox,
  },
  data() {
    return {
      visible: false,
      index: 0,
      galleryImages: [
        {
          src: "recepit-one.jpg",
          img: 'cash-receipt-1.svg',
          title: "Receipt Invoice 1"
        },
        {
          src: "recepit-two.jpg",
          img: 'cash-receipt-2.svg',
          title: "Receipt Invoice 2"
        },
        {
          src: "recepit-three.jpg",
          img: 'cash-receipt-3.svg',
          title: "Receipt Invoice 3"
        },
        {
          src: "recepit-four.jpg",
          img: 'cash-receipt-4.svg',
          title: "Receipt Invoice 4"
        },
      ],
    };
  },
  mounted() {
    var invoiceStars = document.getElementsByClassName("invoice-star");

    for (var i = 0; i < invoiceStars.length; i++) {
      invoiceStars[i].addEventListener("click", function () {
        var parent = this.parentElement.parentElement;
        var invoiceBlogs = document.getElementsByClassName("invoice-blog");

        for (var j = 0; j < invoiceBlogs.length; j++) {
          invoiceBlogs[j].classList.remove("active");
        }

        parent.classList.add("active");
      });
    }
  },
  methods: {
    show(index) {
      this.index = index;
      this.visible = true;
    },
    handlePrev(oldIndex, newIndex) {
      console.log("when prev btn click or user swipe right ----");
      console.log("oldIndex of imgs:", oldIndex);
      console.log("newIndex of imgs:", newIndex);
    },
    handleNext(oldIndex, newIndex) {
      console.log("when next btn click or user swipe left ----");
      console.log("oldIndex of imgs:", oldIndex);
      console.log("newIndex of imgs:", newIndex);
    },
  },
};
</script>
