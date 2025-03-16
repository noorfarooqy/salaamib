<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Form Mask</h5>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title mb-2">Form Mask</h5>
              <p class="card-text">
                Input masks can be used to force the user to enter data conform a
                specific format. Unlike validation, the user can't enter any other key
                than the ones specified by the mask.
              </p>
            </div>
            <div class="card-body">
              <b-form action="javascript:;">

                <div class="form-group">
                  <label>Phone</label>
                  <MaskedInput v-model="phone" class="form-control" :mask="'(999) 999-9999'" />
                  <span class="form-text text-muted">(999) 999-9999</span>
                </div>
                <div class="form-group">
                  <label>Date</label>
                  <MaskedInput v-model="date" class="form-control" :mask="'99 / 99 / 9999'" />
                  <span class="form-text text-muted">dd/mm/yyyy</span>
                </div>
                <div class="form-group">
                  <label>SSN field 1</label>
                  <MaskedInput v-model="ssn" class="form-control" :mask="'999-99-9999'" />
                  <span class="form-text text-muted">e.g "999-99-9999"</span>
                </div>
                <div class="form-group">
                  <label>Phone field + ext.</label>
                  <MaskedInput v-model="phoneExt" class="form-control" :mask="'(999) 999-9999? x99999'" />
                  <span class="form-text text-muted">+40 999 999 999</span>
                </div>
                <div class="form-group">
                  <label>Product Key</label>
                  <MaskedInput v-model="product" class="form-control" :mask="'a*-999-a999'" />
                  <span class="form-text text-muted">e.g a*-999-a999</span>
                </div>
                <div class="form-group">
                  <label>Currency</label>
                  <MaskedInput v-model="currency" class="form-control" :mask="'999,999,999.99'" />
                  <span class="form-text text-muted">$ 999,999,999.99</span>
                </div>
                <div class="form-group">
                  <label>Eye Script</label>
                  <MaskedInput v-model="eyescript" class="form-control" :mask="'~9.99 ~9.99 999'" />
                  <span class="form-text text-muted">~9.99 ~9.99 999</span>
                </div>
                <div class="form-group">
                  <label>Percent</label>
                  <MaskedInput v-model="pct" class="form-control" :mask="'99%'" />
                  <span class="form-text text-muted">e.g "99%"</span>
                </div>
                <div class="form-group mb-0">
                  <label>Credit Card Number</label>
                  <MaskedInput v-model="ccn" class="form-control" :mask="'9999 9999 9999 9999'" />
                  <span class="form-text text-muted">e.g "999.999.999.9999"</span>
                </div>
              </b-form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
import MaskedInput from './MaskedInput.vue';

export default {
  components: {
    MaskedInput,
  },
  name: "app",
  data: () => ({
    date: "",
    phone: "",
    userMask: "aa-aa-AAAA",
    userField: "",
    rawVal: "",
    ssn: "",
    phoneExt: "",
    product: "",
    currency: "",
    eyescript: "",
    pct: "",
    ccn: "",
  }),
}
</script>

<style>
masked-input {
  height: 40px;
}
</style>
