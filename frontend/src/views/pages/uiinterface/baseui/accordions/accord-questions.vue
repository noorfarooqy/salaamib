<template>
  <div class="col-xl-6">
    <div class="accordion custom-accordion" id="custom-accordion-one">
      <div class="card mb-1">
        <div class="card-header" id="headingNine">
          <h5 class="accordion-faq m-0 position-relative">
            <a
              class="custom-accordion-title text-reset d-block"
              data-bs-toggle="collapse"
              href="#collapseNine"
              aria-expanded="true"
              aria-controls="collapseNine"
            >
              Q. Can I use this template for my client?
              <i class="mdi mdi-chevron-down accordion-arrow"></i>
            </a>
          </h5>
        </div>

        <div
          id="collapseNine"
          class="collapse show"
          aria-labelledby="headingFour"
          data-bs-parent="#custom-accordion-one"
        >
          <div class="card-body">
            Yup, the marketplace license allows you to use this theme in any end products.
            For more information on licenses, please refere
            <a href="javascript:;" target="_blank">here</a>.
          </div>
        </div>
      </div>
      <div class="card mb-1">
        <div class="card-header" id="headingFive">
          <h5 class="accordion-faq m-0 position-relative">
            <a
              class="custom-accordion-title text-reset collapsed d-block"
              data-bs-toggle="collapse"
              href="#collapseFive"
              aria-expanded="false"
              aria-controls="collapseFive"
            >
              Q. Can this theme work with Wordpress?
              <i class="mdi mdi-chevron-down accordion-arrow"></i>
            </a>
          </h5>
        </div>
        <div
          id="collapseFive"
          class="collapse"
          aria-labelledby="headingFive"
          data-bs-parent="#custom-accordion-one"
        >
          <div class="card-body">
            No. This is a HTML template. It won't directly with wordpress, though you can
            convert this into wordpress compatible theme
          </div>
        </div>
      </div>
      <div class="card mb-1">
        <div class="card-header" id="headingSix">
          <h5 class="accordion-faq m-0 position-relative">
            <a
              class="custom-accordion-title text-reset collapsed d-block"
              data-bs-toggle="collapse"
              href="#collapseSix"
              aria-expanded="false"
              aria-controls="collapseSix"
            >
              Q. How do I get help with the theme?
              <i class="mdi mdi-chevron-down accordion-arrow"></i>
            </a>
          </h5>
        </div>
        <div
          id="collapseSix"
          class="collapse"
          aria-labelledby="headingSix"
          data-bs-parent="#custom-accordion-one"
        >
          <div class="card-body">
            Use our dedicated support email (support@coderthemes.com) to send your issues
            or feedback. We are here to help anytime
          </div>
        </div>
      </div>
      <div class="card mb-1">
        <div class="card-header" id="headingSeven">
          <h5 class="accordion-faq m-0 position-relative">
            <a
              class="custom-accordion-title text-reset collapsed d-block"
              data-bs-toggle="collapse"
              href="#collapseSeven"
              aria-expanded="false"
              aria-controls="collapseSeven"
            >
              Q. Will you regularly give updates of DGT ?
              <i class="mdi mdi-chevron-down accordion-arrow"></i>
            </a>
          </h5>
        </div>
        <div
          id="collapseSeven"
          class="collapse"
          aria-labelledby="headingSeven"
          data-bs-parent="#custom-accordion-one"
        >
          <div class="card-body">
            Yes, We will update the DGT regularly. All the future updates would be
            available without any cost
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="col-lg-6">
    <p>
      <a
        class="btn btn-primary"
        data-bs-toggle="collapse"
        href="#collapseExample"
        aria-expanded="false"
        aria-controls="collapseExample"
      >
        Link with href
      </a>
      <b-button
        variant="primary ms-2"
        data-bs-toggle="collapse"
        data-bs-target="#collapseExample"
        aria-expanded="false"
        aria-controls="collapseExample"
      >
        Button with data-bs-target
      </b-button>
    </p>
    <div class="collapse show mt-2" id="collapseExample">
      <div class="card">
        <div class="card-body">
          Lorem ipsum is placeholder text commonly used in the graphic, print, and
          publishing industries for previewing layouts and visual mockups.
        </div>
      </div>
    </div>
  </div>
  <!-- end col-->

  <div class="col-lg-6">
    <p>
      <b-button
        variant="primary"
        data-bs-toggle="collapse"
        data-bs-target="#collapseWidthExample"
        aria-expanded="false"
        aria-controls="collapseWidthExample"
      >
        Toggle width collapse
      </b-button>
    </p>
    <div style="min-height: 120px">
      <div class="collapse collapse-horizontal" id="collapseWidthExample">
        <div class="card card-body mb-0 mt-2" style="width: 450px">
          This is some placeholder content for a horizontal collapse. It's hidden by
          default and shown when triggered.
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>
