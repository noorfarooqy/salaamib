<template>
  <div class="invoice-center-pay">
    <div class="receipt-pay-mail">
      <div class="company-logo">
        <img src="@/assets/img/logo.png" alt="Logo" />
      </div>
      <ul>
        <li><span>Hi Company Name,</span></li>
        <li>I’m just getting in touch to follow up on our invoice.</li>
        <li>The invoice is scheduled to be paid on or before (15 Aug 2023).</li>
        <li>
          I look forward to hearing from you and receiving payment shortly. This will
          ensure we can continue to work together.
        </li>
      </ul>
      <div class="click-invoice-btn">
        <router-link to="pay-online" class="btn btn-primary"
          >Click Here to pay Invoice</router-link
        >
      </div>
      <p>Many thanks,</p>
      <p>Finance team</p>
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
