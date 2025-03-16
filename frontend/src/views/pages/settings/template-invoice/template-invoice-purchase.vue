<template>
  <div class="card template-invoice-card">
    <div class="card-body pb-0">
      <div class="invoice-card-title">
        <h6>Purchases</h6>
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
                  :src="require(`@/assets/img/${image.src}`)"
                  alt="Post Image"
                />
              </a>
              <a href="javascript:;" class="preview-invoice image-popup"
                ><i class="fa-regular fa-eye"></i
              ></a>
            </div>
            <div class="invoice-content-title">
              <a href="javascript:;">{{ image.title }}</a>
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
    src: require(`@/assets/img/${image.src}`),
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
          src: "invoice-one.jpg",
          title: "General Invoice 1"
        },
        {
          src: "invoice-two.jpg",
          title: "General Invoice 2"
        },
        {
          src: "invoice-three.jpg",
          title: "General Invoice 3"
        },
        {
          src: "invoice-four.jpg",
          title: "General Invoice 4"
        },
        {
          src: "invoice-five.svg",
          title: "General Invoice 5"
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
